<h2>Django Full Stack Web Application</h2>

<h3>Intro</h3>
<p>The application for requests/tickets/tasks management raised from the need of ecsaping from shared excel files where the risk of getting things messy is very very high. That affects the data quality which has enormous imapct on further reporting and the analysis.</p>

<ul>
 <li>Single django project can have multiple apps (separating blog section and store as both different apps within one web-site)</li>
 <li></li>
 
</ul>

<h3>Application features:</h3>
<ul>
 <li>Object oriented database.</li>
 <li>Post forms data validation.</li>
 <li>User register/login system.</li>
 <li>User profile panel for info updates.</li>
 <li>Access security system.</li>
 <li>Page content filtering.</li>
 <br>
 <img src="images/django.gif">
</ul>


<h3>Demo</h3>
<p>First entry site look.</p>
<img src="images/pr_system.JPG">

<p>All open requests are stored in the Home tab.</p>
<img src="images/pr_home.JPG">

<p>When Purchase Request closed, it goes to the Archive tab.</p>
<img src="images/pr_archive.JPG">

<p>Each buyer can enter a site with ist own Purchase Requests by clicking on the name.</p>
<img src="images/pr_buyer_view.JPG">

<p>Each buyer can access its Purchase Requests and udpdate/delete them.</p>
<img src="images/pr_update.JPG">

<p>Purchase Request number is restricted to be unique in db.</p>
<img src="images/pr_new.JPG">

<h3>Django setup</h3>
<ol>
  <li>Installing django library in venv:
   <br>
   - pip install django
  </li>
  <li>Checking django version:
   <br>
   - python -m django --version
  </li>
  <li>Starting project in project directory:
   <br>
   - django-admin startproject project_name
  </li>
  <li>Running django projects server:
   <br>
   - python manage.py runserver
  </li>
  <li>Creating app:
   <br>
   - python manage.py startapp blog
  </li>
  <li>Data migration (first migration will create a database with default tables):
   <br>
   - python manage.py makemigrations<br>
   - it detects the changes and prepares them to be uploaded to the database
  </li>
  <li>Applying changes to db:
   <br>
   - python manage.py migrate
  </li>
  <li>Creating superuser:
   <br>
   - python manage.py createsuperuser
  </li>
</ol>
