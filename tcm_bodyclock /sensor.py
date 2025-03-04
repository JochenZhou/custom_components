"""Sensor for TCM Body Clock integration."""
from datetime import datetime
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.util import dt as dt_util

from .const import DOMAIN, TCM_HOURS

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensor platform."""
    async_add_entities([TCMBodyClockSensor()])

class TCMBodyClockSensor(SensorEntity):
    """Representation of a TCM Body Clock sensor."""

    _attr_name = "中医养生表"
    _attr_unique_id = "tcm_bodyclock_sensor"
    _attr_icon = "mdi:account-clock"

    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        self._attributes = {}

    @property
    def state(self):
        """Return the current TCM hour."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    def update(self):
        """Update the sensor state and attributes."""
        now = dt_util.now().hour
        for hour in TCM_HOURS:
            if hour["start"] <= now < hour["end"] or (hour["start"] > hour["end"] and (now >= hour["start"] or now < hour["end"])):
                self._state = hour["name"]
                self._attributes = {
                    "经络值班": hour["meridian"],
                    "养生重点": hour["health_tip"],
                    "推荐事项": hour["recommend"],
                    "注意事项": hour["avoid"]
                }
                break