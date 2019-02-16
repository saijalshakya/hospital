import React, { Component } from "react";

const API = 'http://localhost:8000/doc/api/doctor/';

export default class Viewed extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
          hits: [],
          diseases: [],
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

          fetch("http://localhost:8000/doc/api/disease/")
          .then(response => response.json())
          .then(json => {
              this.setState({
                  isLoaded: true,
                  diseases:json
              })
          });
      }
  render() {
      var { isLoaded, items, diseases } = this.state;

      if(!isLoaded){
          return <div>Loading...</div>
      }
      else
      {
        return (
            <div>
                <div className="row">
                    <div className="col-md-8">
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
                                            <a target="_blank">
                                                <img src={item.image} alt="Cinque Terre" width="600" height="400"/>
                                            </a>
                                            <div class="desc">{item.name}</div>
                                        </div>
                                        ))
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="col-md-4">
                        <div class="bg_color_1">
                                <div class="container margin_120_95">
                                    <div className="doctor-view">
                                        <div class="main_title">
                                            <h4>Viral Disease Alert</h4>
                                        </div>
                                        <div className="list-group">
                                        {
                                            diseases.map(disease=>(
                                                <div key={disease.id}>
                                                    {disease.level == "1"? 
                                                        <a href="#" class="list-group-item list-group-item-action list-group-item-danger">{disease.name} - {disease.found}</a>
                                                        :
                                                        <a href="#" class="list-group-item list-group-item-action list-group-item-warning">{disease.name} - {disease.found}</a>                                                     
                                                    }
                                                </div>
                                            ))
                                        }
                                        </div>
                                    </div>
                                </div>
                            </div>
                    </div>
                </div>
            </div>
            );
      }
    
  }
}