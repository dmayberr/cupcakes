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

// async function addCupcake() {
//   const res = await axios.post(`/api/cupcakes`, {
//     flavor: newCupcake.flavor,
//     size: newCupcake.size,
//     rating: newCupcake.rating,
//     image: newCupcake.image,
//   });
//   console.log(res);
// }

async function addCupcake() {
  let flavorinput = $("#flavor").data("flavor");
  let sizeinput = $("#size").data("size");
  let ratinginput = $("#rating").data("rating");
  let imageinput = $("#image").data("image");
  const res = await axios({
    method: "post",
    url: `/api/cupcakes`,
    data: {
      flavor: flavorinput,
      size: sizeinput,
      rating: ratinginput,
      image: imageinput,
    },
  });
  console.log(res);
}
