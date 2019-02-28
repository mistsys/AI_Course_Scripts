##

These scripts are from the Mist “AI for IT” course available from both the Mist Partner portal and the Mist UI.  They build on each other so I the 3rd course is built on top of 1 & 2.

You will need to follow the instructions from the course to setup.  It is highly recommended you create a test org or site to experiment on as mistakes can make things unavailable from the UI as described in the course.  To recover - delete the parent object.

For example if you try to PUT something into a WLAN via the API and it isn’t correct you will see the error shown in the course.  

Solution - Delete the WLAN from either the UI or API and try again.

To do anything you will need to 

1)  Generate and save your Mist API token
2)  Save it as described in the course
3)  Save you <site id>

This will be enough to run check_my_wlans_public.py

Next you will need to create a WLAN that has a simple guest portal created with a PSK.  This will need to be the target WLAN to run change_guest_password_public.py

To run the 3rd script you will need to follow the instructions to setup 2-factor authentic for your test (or personal) gmail account.  The end result of this will be an Google APP Password which will be needed to run the script Change_and_email_public.py

Any questions or suggestions please ping me at matt@mist.com
