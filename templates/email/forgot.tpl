{% block subject %}
	Resetting your ROWViGOR Password
{% endblock %}

{% block body %}

{% endblock %}

{% block html %}

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	    <head>
	        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	        <title>ROWViGOR</title>
	        <meta name="viewport" content="width=device-width" />
	       <style type="text/css">
	            @media only screen and (max-width: 550px), screen and (max-device-width: 550px) {
	                body[yahoo] .buttonwrapper { background-color: transparent !important; }
	                body[yahoo] .button { padding: 0 !important; }
	                body[yahoo] .button a { background-color: #4684b9; padding: 15px 25px !important; }
	            }

	            @media only screen and (min-device-width: 601px) {
	                .content { width: 600px !important; }
	                .col387 { width: 387px !important; }
	            }
	        </style>
	    </head>
	    <body bgcolor="#dfdfdf" style="margin: 0; padding: 0;" yahoo="fix">
	        <!--[if (gte mso 9)|(IE)]>
	        <table width="600" align="center" cellpadding="0" cellspacing="0" border="0">
	          <tr>
	            <td>
	        <![endif]-->

	        <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%; max-width: 600px;" class="content">


	            <tr>
	                <td style="padding: 15px 10px 15px 10px;">

	                </td>
	            </tr>

	            <tr>
	                <td align="center" bgcolor="#F6F8F8" style="padding: 20px 20px 20px 20px; color: #ffffff; font-family: Arial, sans-serif; font-size: 36px; font-weight: bold;">
	                    <img src="https://rowvigor-usa.s3.amazonaws.com/img/row_vigor-blue.png" alt="ROWViGOR Logo"  height="35" style="display:block;" />
	                </td>
	            </tr>
	            <tr>
	                <td align="left" bgcolor="#ffffff" style="padding: 40px 20px 40px 20px;color: #555555;font-family: Avenir Next,Avenir,Helvetica,sans-serif!important;font-size: 16px;line-height: 30px;border-bottom: 1px solid #f6f6f6;">
	                Hello!,
	                 <p>We received your request for a new ROWVIGOR account password. Please click the reset password button below to reset.</p>

					<p>Have more questions, we’re happy to answer! Contact <a href="mailto:support@rowvigor.com" style="color:#21a9df">support@rowvigor.com</a> or give us a call.</p>
					Your ROWViGOR Team <br>

					Web: <a href="http://www.rowvigor.com/" style="color:#21a9df" target="_blank">http://www.rowvigor.com/</a><br>
					Email: <a href="mailto:support@rowvigor.com" style="color:#21a9df">support@rowvigor.com</a><br>
					Phone: <a href="tel:1-877-410-2481" style="color:#21a9df">(703) 477-8805</a><br>


	                </td>
	            </tr>
	            <tr>
	                <td align="center" bgcolor="#f9f9f9" style="padding: 30px 20px 30px 20px; font-family: Arial, sans-serif; border-bottom: 1px solid #f6f6f6;">
	                    <table bgcolor="#354b72" border="0" cellspacing="0" cellpadding="0" class="buttonwrapper">
	                        <tr>
	                            <td align="center" height="50" style=" padding: 0 25px 0 25px; font-family: Arial, sans-serif; font-size: 16px; font-weight: bold;" class="button">
	                                <a href="{{site_url}}/forgot/{{uid}}/{{token}}/?platform=web" style="color: #ffffff; text-align: center; text-decoration: none;">Reset Password</a>
	                            </td>
	                        </tr>
	                    </table>
	                </td>
	            </tr>
	            <tr>
	                <td align="center" bgcolor="#dddddd" style="padding: 15px 10px 15px 10px; color: #555555; font-family: Arial, sans-serif; font-size: 12px; line-height: 18px;">
	                    <b>{{ contact.company }}</b><br/>{{ contact.address }} &bull; {{ contact.city }}, {{ contact.state }} {{ contact.zipcode }}
					<div style="margin-top:10px">
					 <a href = "http://www.facebook.com/rowvigor/" target="_blank" ><img src="https://rowvigor-usa.s3.amazonaws.com/img/facebook-512.png" alt="RowVigor Logo"  height="20"  /></a>&nbsp;

					  <a href = "http://twitter.com/rowvigor" target="_blank" ><img src="https://rowvigor-usa.s3.amazonaws.com/img/icon_twitter.png" alt="Twitter Logo"  height="20" /></a>&nbsp;
					  <a href = "http://instagram.com/rowvigor" target="_blank" ><img src="https://rowvigor-usa.s3.amazonaws.com/img/instagram-512.png" alt="Instagram Logo"  height="20"  /></a>
					</div>
	                    
	                </td>
	            </tr>



	        </table>
	        <!--[if (gte mso 9)|(IE)]>
	                </td>
	            </tr>
	        </table>
	        <![endif]-->
	    </body>

	</html>

{% endblock %}

