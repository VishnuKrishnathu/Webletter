# **Webletter server** 

<details open>
  <summary><b>Table of contents</b></summary>

---

- [Routes](#routes)
- [Demo](#demo)
- [Built with](#built-with)
- [Developing](#developing)
- [Docker](#docker)
- [Continuous Integration](#continuous-integration)

---

</details>

## **Routes**

- /api
- /auth
    - <details open>
        <summary>/register-user</summary>
        <p>Returns a httpOnly cookie with jwt token if the username and email is available and valid</p>
        <strong>METHOD</strong> &nbsp; : &nbsp; POST <br/>
        <strong>BODY</strong> &nbsp; : &nbsp; <br/>

        ```
        {
            username : String,
            email : String,
            full_name : String,
            password : String
        }
        ```
        <strong>RESPONSE</strong> &nbsp; : <br/>
            <ul> STATUS_CODE  &nbsp; (400) : &nbsp; User registeration unsuccessful </ul>
            <ul> STATUS_CODE &nbsp; (200) : &nbsp; User registeration successful </ul>
    </details>

    - <details open>
        <summary>/login-user</summary>
        <p>Returns 200 status code if the user is autorized</p>
        <strong>METHOD</strong> &nbsp; : &nbsp; POST <br/>
        <strong>BODY</strong> &nbsp; : <br/>

        ```
        {
            username : String,
            password : String
        }
        ```

        <strong>RESPONSE</strong> &nbsp; : <br/>
            <ul>STATUS_CODE &nbsp; (400) : &nbsp; User unauthorized</ul>
            <ul>STATUS_CODE &nbsp; (200) : &nbsp; User authorized</ul>

    </details>

<br/>

## **Demo**

[webletter.herokuapp.com/](https://webletter.herokuapp.com/)

<br/>

## **Built with**

- Python
- Django
- Django Rest Framework

<br/>

## **Developing**
Update `.env.example` file found in `authentication_app` and `webletter` with your owm keys and rename it to `.env`

<br/>

### **Docker**
1. Clone this repo with git `git clone https://github.com/VishnuKrishnathu/Webletter.git`
2. `cd Webletter`
3. `docker build .`

<br/>

### Make sure you have python version greater than 3.6.0
- - - -
### **Windows**
- - - -
1. Setup a virtual environtment to run your django project. `python -m venv django-project`
2. Once you’ve created a virtual environment, you may activate it.`django-project\Scripts\activate.bat`
3. [Clone this repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) using git
4. `cd django-project/Webletter`
5. Install the dependencies from the `requirements.txt` file. `pip install -r requirements.txt`
6. Run the server `python manage.py runserver`

<br/>

- - - -
Linux
- - - -
1. Setup a virtual environtment to run your django project. `python -m venv django-project`
2. Once you’ve created a virtual environment, you may activate it.`soruce django-project/bin/activate`
3. [Clone this repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) using git
4. `cd django-project/Webletter`
5. Install the dependencies from the `requirements.txt` file. `pip install -r requirements.txt`
6. Run the server `python manage.py runserver`

<br/>

## **Continuous Integration**
We use [Gtihub Actions](https://github.com/features/actions) for continuous integration. Check out our [built workflows](https://github.com/VishnuKrishnathu/Webletter/actions)