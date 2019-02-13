import React, { Component, Fragment } from 'react';
import { Switch, Route } from "react-router-dom";
import Landing from "./components/landing";
import Nav from "./components/common/Nav";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Nav/>
        <Switch>
          <Route exact path="/" component={Landing} />
        </Switch>
      </Fragment>
    );
  }
}

export default App;
