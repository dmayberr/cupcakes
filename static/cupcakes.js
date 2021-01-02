$(".delete-cupcake").click(deleteCupcake);

async function deleteCupcake() {
  const id = $(this).data("id");
  await axios.delete(`/api/cupcakes/${id}`);
  alert("Deleted");
  $(this).parent().remove();
}

$(".addCupcake").click(addCupcake);

async function addCupcake() {
    let newcupcake = {
        flavor: 
    }    
   
  axios.post("/api/cupcakes", {flavor, size, rating, image});
}
