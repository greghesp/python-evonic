"""Asynchronous Python client for Evonic Fires."""
from __future__ import annotations

import socket

import aiohttp
from yarl import URL

from pyevonic.models import Device


class Evonic:
    """Main class for handling connections with WLED."""

    def __init__(self, host, session=None):
        self.host = host
        self.session = None

        self._client = None
        self.close_session = False
        self._device = None
        self._supports_si_request = None
        self._supports_presets = None

    @property
    def connected(self) -> bool:
        """Return if we are connect to the WebSocket of an Evonic Fire."""
        return self._client is not None and not self._client.closed

    async def connect(self, callback):
        """Connect to the WebSocket of an Evonic Fire"""
        if self.connected:
            return

        if self.session is None:
            self.session = aiohttp.ClientSession()

        url = URL.build(scheme="ws", host=self.host, port=81)

        try:
            self._client = await self.session.ws_connect(url=url)
            await self.listen(callback)

        except (
                aiohttp.WSServerHandshakeError,
                aiohttp.ClientConnectionError,
                socket.gaierror,
        ) as exception:
            raise Exception(
                "Error occurred while communicating with WLED device"
                f" on WebSocket at {self.host}"
            ) from exception

    async def listen(self, callback):
        if not self._client:
            raise Exception("Not connected to a WLED WebSocket")

        while not self._client.closed:
            message = await self._client.receive()

            if message.type == aiohttp.WSMsgType.ERROR:
                raise Exception(self._client.exception())

            if message.type == aiohttp.WSMsgType.TEXT:
                message_data = message.json()

                if self._device is None:
                    self._device = Device(message_data)

                # print(message_data)
                device = self._device.update_from_dict(message_data)
                callback(device)

            if message.type in (
                    aiohttp.WSMsgType.CLOSE,
                    aiohttp.WSMsgType.CLOSED,
                    aiohttp.WSMsgType.CLOSING,
            ):
                raise Exception(
                    f"Connection to the WLED WebSocket on {self.host} has been closed"
                )

    async def disconnect(self) -> None:
        """Disconnect from the WebSocket of a WLED device."""
        if not self._client or not self.connected:
            return

        await self._client.close()

