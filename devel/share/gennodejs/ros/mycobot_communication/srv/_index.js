
"use strict";

let GetCoords = require('./GetCoords.js')
let PumpStatus = require('./PumpStatus.js')
let GripperStatus = require('./GripperStatus.js')
let SetAngles = require('./SetAngles.js')
let SetCoords = require('./SetCoords.js')
let GetAngles = require('./GetAngles.js')

module.exports = {
  GetCoords: GetCoords,
  PumpStatus: PumpStatus,
  GripperStatus: GripperStatus,
  SetAngles: SetAngles,
  SetCoords: SetCoords,
  GetAngles: GetAngles,
};
