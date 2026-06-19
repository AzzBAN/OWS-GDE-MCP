---
name: ows-new-service
description: Checklist and patterns for building a new OWS service element. Use when asked to create or design a service.
---

# OWS New Service Skill

## Before You Start

1. **Understand the data model** — use `get_model_fields(tenant, asset_uri)` to know what fields are available
2. **Check existing services** — use `list_services(tenant, project, module)` to find similar services to reference
3. **Clarify input/output** — what does the caller pass in, what should come back?

## Service Flow Patterns

### Query / List service
```
Input → [Validate Input] → [Build TQL] → [Query Model] → [Transform Output] → Output
```
- Use a `QueryModel` step with TQL
- Always paginate: accept `start` + `limit` in input, return `total` + `data[]`

### Create / Update service
```
Input → [Validate] → [Check Permissions] → [Write Model] → [Trigger Side Effects] → Output
```
- Use `CreateData` or `UpdateData` steps
- Return the created/updated record ID

### Invoke external / orchestration service
```
Input → [Prepare Request] → [RunScript: build payload] → [InvokeService: target] → [Handle Response] → Output
```
- Use `RunScript` (Rhino2/JS) for payload transformation
- Use `InvokeService` step to call other services

## RunScript Conventions

```javascript
// Access input fields
var fieldValue = input.get("fieldName");

// Set output fields  
output.put("result", value);

// Log for debugging
logger.info("Processing: " + fieldValue);

// Throw on validation failure
if (!fieldValue) {
    throw new Error("fieldName is required");
}
```

## Checklist

- [ ] Input schema defined (field names, types, required/optional)
- [ ] Output schema defined
- [ ] `open_level` set correctly (public / protected / private)
- [ ] Error handling in RunScript steps
- [ ] Tested via `invoke_service` on testbed before deploying

## Notes

- Service names use snake_case: `centralize_inquiry_ticket_get_list`
- Prefix with module abbreviation for discoverability: `cit_`, `cm_`, `inc_`
- Keep services single-purpose — one service, one responsibility
