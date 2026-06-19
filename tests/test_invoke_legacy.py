from ows_gde_mcp.tools.live import _service_invoke_path


def test_project_scoped_path():
    p = _service_invoke_path(
        "IOH_Service_Forecast_Order", "IOH_Service_Forecast_Order", "sfo_x_getList"
    )
    assert p == (
        "/adc-service/rest/v1/services/IOH_Service_Forecast_Order/"
        "IOH_Service_Forecast_Order/sfo_x_getList"
    )


def test_legacy_path_when_no_project_module():
    p = _service_invoke_path("", "", "cmdb_site_getList")
    assert p == "/adc-service/rest/v1/legacy/services/cmdb_site_getList"
