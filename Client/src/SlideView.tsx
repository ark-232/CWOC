import { Transition, TransitionStatus } from 'react-transition-group'
import React, { Component } from "react"

const duration = 1000;

const defaultStyle = {
  transition: `opacity ${duration}ms ease-in-out`,
  opacity: 0,
}

const transitionStyles: {entering: React.CSSProperties, entered: React.CSSProperties, exiting: React.CSSProperties, exited: React.CSSProperties} = {
  entering: { opacity: 1},
  entered:  { opacity: 1 },
  exiting:  { opacity: 0 },
  exited:  { opacity: 0 },
};

function retrieveStyle(ident: TransitionStatus) {
  switch (ident) {
    case "entering":
      return transitionStyles.entering
    case "entered":
      return transitionStyles.entered
    case "exiting":
      return transitionStyles.exiting
    case "exited":
      return transitionStyles.exited
  }
}

export interface SlideProps {
  in: boolean
  children: string
}

export interface SlideState {
  in: boolean
}

export class Slide extends Component<SlideProps, SlideState> {
  constructor(props: SlideProps) {
    super(props)
  }

  render() {
    console.log(this.props)
    return (
      <Transition in={this.props.in} timeout={duration}>
        {state => (
          <div style={retrieveStyle(state)}>
            {this.props.children}
          </div>
        )}
      </Transition>
    )
  }
}
