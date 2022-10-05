# Device Registry Service

## Usage

All responses will have the form

```json
{
  "data": "Mixed type holding the content of the response",
  "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all devices

**Definition**

`GET /devices`

**Response**

- `200 OK` on success

```json
[
  {
    "id": "living-room",
    "name": "Living Room",
    "device_type": "Light",
    "controller_gateway": "192.1.68.0.2"
  }
]
```

### Registering a new device

**Definition**

`POST /devices`

**Arguments**

- `"id":string` a unique identifier for this device
- `"name":string` a name for this device
- `"device_type":string` the type of the device
- `"controller_gateway":string` the IP address of the devices controller

If a device with the given id already exists, that device will be overwritten

**Response**

- `201 Created` on success

```json
{
  "id": "living-room",
  "name": "Living Room",
  "device_type": "Light",
  "controller_gateway": "192.1.68.0.2"
}
```

## Lookup device details

`GET /device/<id>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
  "id": "living-room",
  "name": "Living Room",
  "device_type": "Light",
  "controller_gateway": "192.1.68.0.2"
}
```

## Delete a device

**Definition**

`DELETE /device/<id>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` On success
