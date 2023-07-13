$(document).ready(function () {
    $('#generar').click(function () {

        const listUsers = async () => {
            const response = await fetch("https://jsonplaceholder.typicode.com/users");
            const users = await response.json();

            let tablebody = ``;

            users.forEach((user, index) => {
                tablebody +=
                    `<tr>
                <td>${user.id}</td>
                <td>${user.name}</td>
                <td>${user.username}</td>
                <td>${user.email}</td>
                <td>${user.phone}</td>
                </tr>`
            })

            tabla_users.innerHTML = tablebody;
        };

        listUsers();
    });
})  