import React from "react"
import Controller from "./Controller"

const ContContext = React.createContext<Controller>(new Controller())
export const ControllerContext = ContContext.Consumer
export const ControllerContextProvider = ContContext.Provider
