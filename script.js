//
var store = [];
var count =0;
window.addEventListener("load" , ()=>{
	const input = document.getElementById("upload");
	const filewrapper =  document.getElementById("filewrapper");
	
	input.addEventListener("change" , (e)=>{
		let filename = e.target.files[0].name;
		let filetype = e.target.value.split('.').pop();
		fileshow(filename, filetype);
		//save input files in array
	
		var file = input.files[0];
		var read = new FileReader();
		read.readAsDataURL(file);
		read.addEventListener('load', ()=>{
			var temporary = read.result;
			store[count] = temporary;
			count++;
		})
		
		//end of saving file
	})

	const  fileshow = (filename,filetype)=> {
		const showfileboxElement = document.createElement("div");
		showfileboxElement.classList.add("showfilebox");
		const leftElement  = document.createElement("div");
		leftElement.classList.add("left");
		const fileTypeElement = document.createElement("span");
		fileTypeElement.classList.add("filetype");
		fileTypeElement.innerHTML = filetype;
		const fileTitleElement = document.createElement("h3");
		fileTitleElement.innerHTML = filename;
		leftElement.append(fileTitleElement);
		showfileboxElement.append(leftElement);
		const rightElement = document.createElement("div");
		rightElement.classList.add("right");
		showfileboxElement.append(rightElement);
		const crossElement = document.createElement("span");
		crossElement.innerHTML = "&#215;";
		rightElement.append(crossElement);
		filewrapper.append(showfileboxElement);

		crossElement.addEventListener("click", ()=>{
			filewrapper.removeChild(showfileboxElement);
			count--;
		})

		
	}

})

function print_console(){
	myfunction();
}

var Input =  document.getElementById('photo');
var temp;
// fetching the image from browser and converting the image to base64 
function genUrl()
{
   var file = Input.files[0];
   var reader = new FileReader();
   reader.readAsDataURL(file);
   reader.addEventListener('load', ()=> {
	   temp =reader.result;
	   myfunction();
   });
}
//Converting the base64 to pdf file and uploading the file to the browser
function upload_file(base64_pdf_val)
{
	const binaryString = atob(base64_pdf_val.split(",")[1]);
	const uint8Array = new Uint8Array(binaryString.length);
	for (let i = 0; i < binaryString.length; i++) {
	  uint8Array[i] = binaryString.charCodeAt(i);
	}
	const blob = new Blob([uint8Array], { type: "application/pdf" });
	const url = URL.createObjectURL(blob);
  //console.log(url);
  const a = document.getElementById("download");
	a.href = url;
	a.download = 'hitesh.pdf';
}
//sending a post request to the backend flask application for convertion of img to pdf
function myfunction(){
   var value = store;
   
   $.ajax({
	   url: '/process',
	   type: 'POST',
	   contentType: 'application/json',
	   data: JSON.stringify({'value':  value}),
	   success: function(response){

		  // document.getElementById('output').innerHTML = response;
		   upload_file(response);
	   },
	   error: function(error){
		   console.log(error);
	   }
   });
   }