"""Curated catalog of verified read-only OWS services.

Ported from knowledge-helper/src/ows/catalog.ts. Services listed here are
allowed by `service_guard.assert_read_service` even if their name lacks a
read suffix. Extend this list only with services confirmed to be reads.
"""

from __future__ import annotations

SERVICE_CATALOG: list[dict[str, str]] = [
    {
        "service": "cmdb_site_getList",
        "type": "legacy",
        "notes": "CMDB site master — pid, name, projectid, area_id, ...",
    },
    {
        "service": "cmdb_fm_office_getList",
        "type": "legacy",
        "notes": "FM office lookup — id, fm_office_name, keycode, ...",
    },
    {
        "service": "sfc_service_forecast_order_process_getList",
        "project": "IOH_Service_Forecast_Order",
        "module": "IOH_Service_Forecast_Order",
        "type": "project",
        "notes": "SFO ticket/workflow process records.",
    },
]

CATALOG_SERVICE_NAMES: frozenset[str] = frozenset(e["service"] for e in SERVICE_CATALOG)
