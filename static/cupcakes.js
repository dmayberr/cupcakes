$(".delete-cupcake").click(deleteCupcake);

async function deleteCupcake() {
  const id = $(this).data("id");
  await axios.delete(`/api/cupcakes/${id}`);
  alert("Deleted");
  $(this).parent().remove();
}

$(".addCupcake").click(addCupcake);

function getFormData() {
  let flavorinput = $("#flavor").data("flavor");
  let sizeinput = $("#size").data("size");
  let ratinginput = $("#rating").data("rating");
  let imageinput = $("#image").data("image");

  newCupcake = {
    flavor: flavorinput,
    size: sizeinput,
    rating: ratinginput,
    image: imageinput,
  };

  return newCupcake;
}

async function addCupcake() {
  let flavorinput = $("#flavor").val();
  let sizeinput = $("#size").val();
  let ratinginput = $("#rating").val();
  let imageinput = $("#image").val();
  const res = await axios.post(`http://127.0.0.1:5000/api/cupcakes`, {
    flavorinput,
    sizeinput,
    ratinginput,
    imageinput,
  });
  console.log(res);
}
