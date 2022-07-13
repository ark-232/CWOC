import React from 'react';
import Controller from "./Controller"
import { render, screen } from '@testing-library/react';
import View from './View';

test('renders learn react link', () => {
  render(<View controller={new Controller()} />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
