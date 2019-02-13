import React, { Component } from "react";

const API = 'http://localhost:8000/doc/api/doctor/';

export default class Viewed extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
          hits: [],
          isLoaded:false
        };
      }
    
      componentDidMount() {
        fetch(API)
          .then(response => response.json())
          .then(json => {
              this.setState({
                  isLoaded: true,
                  items:json
              })
          });
      }
  render() {
      var { isLoaded, items } = this.state;

      if(!isLoaded){
          return <div>Loading...</div>
      }
      else
      {
        return (
            <div class="bg_color_1">
                <div class="container margin_120_95">
                    <div className="doctor-view">
                        <div class="main_title">
                            <h2>Most Viewed doctors</h2>
                            <p>Usu habeo equidem sanctus no. Suas summo id sed, erat erant oporteat cu pri.</p>
                        </div>
                        {
                            items.map(item=>(
                                <div class="gallery" key={item.id}>
                                <a target="_blank" href="img_5terre.jpg">
                                    <img src={item.image} alt="Cinque Terre" width="600" height="400"/>
                                </a>
                                <div class="desc">{item.name}</div>
                            </div>
                            ))
                        }
                    </div>
                </div>
            </div>
            );
      }
    
  }
}