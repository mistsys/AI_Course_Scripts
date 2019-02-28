{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 Helvetica-Bold;\f2\fnil\fcharset0 HelveticaNeue;
\f3\fswiss\fcharset0 Helvetica-BoldOblique;}
{\colortbl;\red255\green255\blue255;\red10\green77\blue204;\red244\green246\blue249;}
{\*\expandedcolortbl;;\cssrgb\c1176\c40000\c83922;\cssrgb\c96471\c97255\c98039;}
\margl1440\margr1440\vieww24560\viewh17700\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs34 \cf0 ##\
\
These scripts are what we ran in the Mist \'93AI for IT\'94 course available from both the Mist Partner portal and the Mist UI.\
\
You will need to follow the instructions from the course to setup.  It is 
\f1\b highly recommended
\f0\b0  you create a test org or site to experiment on as mistakes can make things unavailable from the UI as described in the course.  To recover - delete the parent object.\
\
For example if you try to PUT something into a WLAN via the API and it isn\'92t correct you will see the error shown in the course.  \
\
Solution - Delete the WLAN from either the UI or API and try again.\
\
To do anything you will need to \
\
1)  Generate and save your Mist API token\
2)  Save it as described in the course\
3)  Save you <site id>\
\
This will be enough to run {\field{\*\fldinst{HYPERLINK "https://github.com/mistsys/AI_Course_Scripts/blob/master/check_my_wlans_public.py"}}{\fldrslt 
\f2\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 check_my_wlans_public.py}}
\f2\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs34 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 Next you will need to create a WLAN that has a simple guest portal created with a PSK.  This will need to be the target WLAN to run {\field{\*\fldinst{HYPERLINK "https://github.com/mistsys/AI_Course_Scripts/blob/master/change_guest_password_public.py"}}{\fldrslt 
\f2\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 change_guest_password_public.py}}
\f2\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\

\f0\fs34 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 To run the 3rd script you will need to follow the instructions to setup 2-factor authentic for your test (or personal) gmail account.  The end result of this will be an 
\f3\i\b Google APP Password
\f0\i0\b0  which will be needed to run the script {\field{\*\fldinst{HYPERLINK "https://github.com/mistsys/AI_Course_Scripts/blob/master/Change_and_email_public.py"}}{\fldrslt 
\f2\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Change_and_email_public.py}}
\f2\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf2 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs34 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 Any questions or suggestions please ping me at matt@mist.com
\f2\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
}