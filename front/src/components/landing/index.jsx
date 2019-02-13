import React, { Component, Fragment } from "react";
import Banner from "./banner";
import Viewed from "./viewed";

export default class Landing extends Component {
    render() {
      return (
        <Fragment>
          <Banner/>
          <Viewed/>
        </Fragment>
      );
    }
  }