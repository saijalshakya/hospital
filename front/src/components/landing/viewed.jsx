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
                        {/* <div class="bg_color_1">
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
                        </div> */}
                        <div class="bg_color_1">
                            <div class="container margin_120_95">
                                <h2>Welcome</h2>
                                <hr/>
                                <div className="box">
                                    <h6  class="text-justify font-weight-normal">The history of private hospital in Nepal dates back to late 1980's .After the people's popular movement 1990 AD. There was mushrooming of private hospitals or nursing homes. Nearing to people popular movement 2062 BS (April,2006 AD) ,There was sprouting yet another hospital Called Alka Hospital in the heart of the lalitpur district .Question is : Is the hospital different from others ? Or why do people from valley need additional Hospital like this ?

To answer this question let us go a deeper down to its conception and the path it has taken till it took the shape of the hospital.</h6>
                                <br/>
                                <br/>
                                <button className="btn btn-primary btn-lg">Read More ></button>
                                <a href="http://www.alkahospital.com/uploads/files/Alkahospital_Rate_list_01042074.pdf" target="_blank"><button className="btn btn-primary btn-lg">Price List</button></a>
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