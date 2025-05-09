document.getElementById("update-form").addEventListener("submit", async function(event) {
  event.preventDefault(); 

  const form = event.target;
  const formData = new FormData(form);

  const data = {};
  formData.forEach((value, key) => {
    data[key] = value;
  });

  const urlParams = new URLSearchParams(window.location.search);
  const post_id = urlParams.get('post_id');

  try {
    const response = await fetch(`/update?post_id=${post_id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if (response.ok) {
      const result = await response.json();
      console.log('Success:', result);
      window.location.href = '/';
    } else {
      console.error('Server error:', response.statusText);
    }
  } catch (error) {
    console.error('Request failed:', error);
  }
});


