const api_url = 'https://api.seaofkeys.com/stats/users';


// Define the session cookies as an object
const session_cookies = {
  session_id: 'c9a85e1f-ee25-4686-aea0-ae3c65041621',
};

// Create a Headers object and add the cookies to it
const headers = new Headers();
for (const cookieName in session_cookies) {
  headers.append('Cookie', `${cookieName}=${session_cookies[cookieName]}`);
}

// Define the URL for the fetch request


// Define the fetch request
fetch(api_url, {
  method: 'GET',
  headers: headers,
})
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Network response was not ok');
    }
  })
  .then(data => {
    // Handle the response data here
    console.log(data);
  })
  .catch(error => {
    // Handle errors here
    console.error('There was a problem with the fetch operation:', error);
  });