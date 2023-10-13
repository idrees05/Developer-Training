
// Nested Objects for Employee and Library
const employee = {
    id: 1,
    name: 'John Doe',
    position: 'Software Engineer',
    department: {
        name: 'Engineering',
        location: 'Building A',
        supervisor: {
            name: 'Jane Smith',
            position: 'Engineering Manager'
        }
    }
};

const library = {
    name: 'Public Library',
    location: 'City Center',
    books: [
        {
            id: 'B001',
            title: 'The Great Gatsby',
            author: 'F. Scott Fitzgerald',
            details: {
                genre: 'Fiction',
                year: 1925
            }
        },
        {
            id: 'B002',
            title: 'To Kill a Mockingbird',
            author: 'Harper Lee',
            details: {
                genre: 'Fiction',
                year: 1960
            }
        }
    ]
};

// Accessing the specified properties
let johns_supervisor = employee.department.supervisor.name;
let great_gatsby_title = library.books[0].title;

// Displaying the results in the HTML
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("supervisorName").innerText = "John's Supervisor: " + johns_supervisor;
    document.getElementById("gatsbyTitle").innerText = "Title of the Book: " + great_gatsby_title;
});
