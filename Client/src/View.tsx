import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'
import {ControllerContext, ControllerContextProvider} from "./ControllerContext"
import Controller from "./Controller"
import logo from "./logo512.png"
import { Slide } from "./SlideView"

export interface ViewProps {
  controller: Controller
}

export interface ViewState {
  controller: Controller
  overlay: Component | null
  page: boolean
}

class View extends Component<ViewProps, ViewState> {
  constructor(props: ViewState) {
    super(props)
    this.state = {
      controller: props.controller,
      overlay: null,
      page: true
    }
  }

  render() {
    console.log(this.state.page)
    return (
      <ControllerContextProvider value={this.state.controller}>
        <Slide in={this.state.page}>h</Slide>
        <Button variant="primary" onClick={() => this.setState({page: !this.state.page})}>Toggle</Button>
      </ControllerContextProvider>
    )
  }
}

export default View;
