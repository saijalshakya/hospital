import React, { Component } from "react";
import axios from "axios";

export default class Banner extends Component {
	constructor(props){
		super(props)

		
		this.state = {
			name: null,
			loading:false,
			message:""
		}
	}

	handleSubmit = (event) => {
		event.preventDefault()

		const name = this.state.name

		this.setState({
			loading:true
		})

		const data = {
			name
		}
		axios.post("/t/tt6u5-1550666534/post", data)
			.then(response => {
				console.log("sa"+response.data)
				this.setState({
					loading:false,
					message:response.data
				})
			})
			.catch(er => {
				console.log("er"+er)
				this.setState({
					loading:false
				})
			})
	}

	handleInputChange = (event) => {
		event.preventDefault()

		this.setState({
			[event.target.name]: event.target.value
		})
	}

	loadOrShowing(){
		if (this.state.loading)
		{
			return <p>Loading...</p>
		}
		else
		{
			return <p>{this.state.message}</p>
		}
	}
  render() {
    return (
        <main>
						<div class="hero_home version_1">
							<div class="content">
								<h3>Find a Doctor!</h3>
										<p>
										</p>
								<form onSubmit={this.handleSubmit.bind(this)}>
									<div id="custom-search-input">
										<div class="input-group">
									<input type="text" class=" search-query" name="name" value={this.state.name} onChange={this.handleInputChange.bind(this)} placeholder="Ex. Name, Specialization ...."/>
									<input type="submit" class="btn_search" value="Search"/>
								</div>
							</div>
						</form>
					</div>
				</div>
				{this.loadOrShowing()}
        </main>
    );
  }
}