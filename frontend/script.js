const API =
"https://ubiquitous-barnacle-6j9jjjpgpxvf5qx6-8000.app.github.dev";

async function register(){

    const data = {
        username:
        document.getElementById("reg_username").value,

        email:
        document.getElementById("reg_email").value,

        password:
        document.getElementById("reg_password").value
    };

    const response = await fetch(
        API + "/api/v1/auth/register",
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(data)
        }
    );

    const result = await response.json();

    document.getElementById("message").innerText =
    JSON.stringify(result);
}


async function login(){

    const data = {
        email:
        document.getElementById("login_email").value,

        password:
        document.getElementById("login_password").value
    };

    const response = await fetch(
        API + "/api/v1/auth/login",
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(data)
        }
    );

    const result = await response.json();

    if(response.ok){
        localStorage.setItem(
            "token",
            result.access_token
        );

        window.location =
        "dashboard.html";
    }else{
        document.getElementById("message").innerText =
        result.detail;
    }
}


async function createTask(){

    const token =
    localStorage.getItem("token");

    const response = await fetch(
        API + "/api/v1/tasks/",
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json",
                "Authorization":
                "Bearer " + token
            },
            body:JSON.stringify({
                title:
                document.getElementById("title").value,

                description:
                document.getElementById("description").value
            })
        }
    );

    loadTasks();
}


async function loadTasks(){

    const token =
    localStorage.getItem("token");

    const response = await fetch(
        API + "/api/v1/tasks/",
        {
            headers:{
                "Authorization":
                "Bearer " + token
            }
        }
    );

    const tasks =
    await response.json();

    let html = "";

    tasks.forEach(task=>{

        html += `
        <div>
            <h3>${task.title}</h3>
            <p>${task.description}</p>

            <button onclick="deleteTask(${task.id})">
            Delete
            </button>
        </div>
        `;
    });

    document.getElementById("tasks").innerHTML =
    html;
}


async function deleteTask(id){

    const token =
    localStorage.getItem("token");

    await fetch(
        API + "/api/v1/tasks/" + id,
        {
            method:"DELETE",
            headers:{
                "Authorization":
                "Bearer " + token
            }
        }
    );

    loadTasks();
}

function logout(){
    localStorage.removeItem("token");
    window.location = "index.html";
}