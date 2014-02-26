Title: Contact
Tags: Contact
Status: hidden
Author: Omphalosskeptic
Summary: Contact Us

<style>
form{
	max-width: 600px;
	margin: 0 auto;
}

input, textarea{
	border: 1px solid #ddd;
	font-family: serif;
	padding:7px !important;
	font-size: 1em;
}

input:focus, textarea:focus{
	border: 1px solid orange;
}

form fieldset {
	margin: 0 0 10px 0;
	padding: 0 0 10px 0;
	/*border-bottom: 1px dashed #eee;*/
}

form fieldset.form-actions {
	margin: 0 0 0 40%;
	padding: 0;
	border: none;
}

form fieldset label {
	float: left;
	width: 30%;
	margin: 4px 0 5px 0;
	/*font-weight: bold;*/
	-moz-font-feature-settings:"smcp" 1; 
	-moz-font-feature-settings:"smcp=1"; 
	-ms-font-feature-settings:"smcp" 1; 
	-o-font-feature-settings:"smcp" 1; 
	-webkit-font-feature-settings:"smcp" 1; 
	font-feature-settings:"smcp" 1;
	text-transform: lowercase;
	font-variant: small-caps;
}

form fieldset input.form-text,
form fieldset textarea {
	display: block;
	width: 70%;
}

form fieldset textarea {
	height: 150px;
}

form fieldset p.form-help {
	margin: 5px 0 0 20%;
	font-size: 12px;
	color: #999;
}
form input[type="submit"] {
	margin: 0;
	padding: 10px 15px;
	border: 1px solid #ccc;
	background: #eee;
	text-transform: lowercase;
	font-variant: small-caps;
	font-weight: bold;
	border-radius: 2px;
}
form input[type="submit"]:hover,
form input[type="submit"]:focus {
	border: 1px solid #bbb;
	background: #e5e5e5;
}
form input[type="submit"]:active {
	borde r: 1px solid #ccc;
	background: #eee;
}

@media screen and (max-width: 960px) {
	form fieldset label {
		display: block;
		float: none;
		width: auto;
		margin: 0 0 5px 0;
		}
	form fieldset.form-actions,
	form fieldset p.form-help {
		margin-left: 0;
		padding-left: 0;
		}
	form fieldset input.form-text,
	form fieldset textarea {
		width: 100%;
		-webkit-box-sizing: border-box;
		-moz-box-sizing: border-box;
		box-sizing: border-box;
		}
	}				
</style>

Say “Hello”, send a plea for help, wax eloquent on Science Class’s grammatical errors, or find another way to make life interesting for the folks running it.

<form class="contactform" action="//api.formspree.com/info@automathic.org" method="POST">
	<fieldset>
		<label for="input-name">Your Name</label>
    	<input class="form-text" id="input-name" type="text" name="name" placeholder="Joe Smith" required>
    </fieldset>
  	<fieldset>
		<label for="input-email">Your Email</label>
    	<input class="form-text" id="input-email" type="email" name="_replyto" placeholder="email@example.com">
    </fieldset>
    <input type="hidden" name="_next" value="//scienceclass.github.io/pages/thanks.html">
    <fieldset>
		<label for="input-message">Your Message</label>
    	<textarea id="input-message" name="message" placeholder="I ❤ Science Class" required></textarea>
    </fieldset>
    <fieldset class="form-actions">
    	<input type="submit" value="SEND &raquo;">
    </fieldset>
</form> 