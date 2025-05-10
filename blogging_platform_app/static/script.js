// Update PUT Function

document.addEventListener("DOMContentLoaded", () => {
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
        window.alert("Post Updated Successfully")
        window.location.href = '/';
      } else {
        console.error('Server error:', response.statusText);
      }
    } catch (error) {
      console.error('Request failed:', error);
    }
  });
});

// Delete DELETE Function

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".delete-form").forEach(form => {
    form.addEventListener("submit", async function(event) {
      event.preventDefault(); 

      const post_id = new URL(form.action).searchParams.get("post_id");

      const confirmed = confirm(`Are you sure you want to delete Post: ${post_id} ?`);
      if (!confirmed) return;

      try {
        const response = await fetch(`/delete?post_id=${post_id}`, {
          method: 'DELETE'
        });

        if (response.ok) {
          alert("Post deleted successfully");
          window.location.href = "/";
        } else {
          console.error('Server error:', response.statusText);
        }
      } catch (error) {
        console.error('Request failed:', error);
      }
    });
  });
});