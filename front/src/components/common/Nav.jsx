import React, { Component } from "react";
import { NavLink, Link } from "react-router-dom";

class Nav extends Component {
    render() {
        return (
            <header class="header_sticky">	
		<a href="#menu" class="btn_mobile">
			<div class="hamburger hamburger--spin" id="hamburger">
				<div class="hamburger-box">
					<div class="hamburger-inner"></div>
				</div>
			</div>
		</a>
		<div class="container">
			<div class="row">
				<div class="col-lg-3 col-6">
					<div id="logo_home">
						<h1><a href="../findoctor/index.html" title="Findoctor">Hospital</a></h1>
					</div>
				</div>
				<div class="col-lg-9 col-6">
					<ul id="top_access">
						<li><a href="../findoctor/login.html"><i class="pe-7s-user"></i></a></li>
						<li><a href="../findoctor/register-doctor.html"><i class="pe-7s-add-user"></i></a></li>
					</ul>
					<nav id="menu" class="main-menu">
						<ul>
							<li>
                                <span><NavLink to="/">Home</NavLink></span>
									
							</li>
							<li>
								<span><a href="#0">Pages</a></span>
								<ul>
									<li>
										<span><a href="#0">List pages</a></span>
										<ul>
											<li><a href="../findoctor/list.html">List page</a></li>
											<li><a href="../findoctor/grid-list.html">List grid page</a></li>
											<li><a href="../findoctor/list-map.html">List map page</a></li>
										</ul>
									</li>
									<li>
										<span><a href="#0">Detail pages</a></span>
										<ul>
											<li><a href="../findoctor/detail-page.html">Detail page</a></li>
											<li><a href="../findoctor/detail-page-2.html">Detail page 2</a></li>
                                    		<li><a href="../findoctor/detail-page-3.html">Detail page 3</a></li>
											<li><a href="../findoctor/detail-page-working-booking.html">Detail working booking</a></li>
										</ul>
									</li>
									<li><a href="../findoctor/submit-review.html">Submit Review</a></li>
									<li><a href="../findoctor/blog-1.html">Blog</a></li>
									<li><a href="../findoctor/badges.html">Badges</a></li>
									<li><a href="../findoctor/login.html">Login</a></li>
									<li><a href="../findoctor/login-2.html">Login 2</a></li>
									<li><a href="../findoctor/register-doctor.html">Register Doctor</a></li>
									<li><a href="../findoctor/register-doctor-working.html">Working doctor register</a></li>
									<li><a href="../findoctor/register.html">Register</a></li>
									<li><a href="../findoctor/about.html">About Us</a></li>
									<li><a href="../findoctor/contacts.html">Contacts</a></li>
								</ul>
							</li>
							<li>
								<span><a href="#0">Extra Elements</a></span>
								<ul>
                                	<li><a href="../findoctor/detail-page-working-booking.html">Detail working booking</a></li>
                                    <li><a href="../findoctor/booking-page.html">Booking page</a></li>
                                    <li><a href="../findoctor/confirm.html">Confirm page</a></li>
                                	<li><a href="../findoctor/faq.html">Faq page</a></li>
                                    <li><a href="../findoctor/coming_soon/index.html">Coming soon</a></li>
                                    <li>
										<span><a href="#0">Pricing tables</a></span>
										<ul>
											<li><a href="../findoctor/pricing-tables-3.html">Pricing tables 1</a></li>
                                    		<li><a href="../findoctor/pricing-tables.html">Pricing tables 2</a></li>
                                    		<li><a href="pricing-tables-2.html">Pricing tables 3</a></li>
										</ul>
									</li>
									<li><a href="con-pack-1.html">Icon pack 1</a></li>
									<li><a href="icon-pack-2.html">Icon pack 2</a></li>
									<li><a href="icon-pack-3.html">Icon pack 3</a></li>
									<li><a href="404.html">404 page</a></li>
								</ul>
							</li>
                            <li><span><a href="menu_2/index.html">Menu V2</a></span></li>
							<li><span><a href="admin_section/index.html" target="_blank">Admin</a></span></li>
							<li><span><a href="https://themeforest.net/item/findoctor-doctors-directory-and-book-online-template/20876478?ref=ansonika">Buy this template</a></span></li>
						</ul>
					</nav>
				</div>
			</div>
		</div>
	</header>
        )
    }
}

export default Nav;