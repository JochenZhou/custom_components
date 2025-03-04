"""Config flow for TCM Body Clock integration."""
from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN

class TCMBodyClockConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for TCM Body Clock."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="中医养生表", data={})

        return self.async_show_form(
            step_id="user",
            description_placeholders={"description": "点击确认添加中医养生表组件"}  # 修复拼写错误
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return TCMBodyClockOptionsFlow(config_entry)

class TCMBodyClockOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for TCM Body Clock."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional("alert_enabled", default=True): bool
            })
        )