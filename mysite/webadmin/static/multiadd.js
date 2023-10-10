document.addEventListener("DOMContentLoaded", function(){

  var url = "https://api.seaofkeys.com"
  var addItemTop = document.getElementById("addItem");

  function getvals(id, endpoint){
    return fetch(url +  endpoint + id ,
    {
      method: "GET",
      headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      },
    })
    .then((response) => response.json())
    .then((responseData) => {		  
      return responseData;
    })
    .catch(error => console.warn(error));
    }  
  
    function setResponse(response){      
      
      var parent = document.getElementById("mySelectOptions");
      var multiTemplateInput = document.getElementById("multiTemplateInputEdit");
      var multiTemplateLabel = document.getElementById("multiTemplateLabelEdit");
  
      parent.innerHTML = "";   
  
      response.forEach(function (item){
  
        const inputClone = multiTemplateInput.cloneNode(true);       
        const labelClone = multiTemplateLabel.cloneNode(true);     
  
        const newDiv = document.createElement("div");
        newDiv.classList.add("d-flex");
  
        parent.appendChild(newDiv);
  
        inputClone.value = item.id;
        labelClone.innerHTML = item.name;
  
        labelClone.classList.add("m-0");
        labelClone.classList.add("m-1");
  
        inputClone.style.display = "block";
        labelClone.style.display = "block";
  
        inputClone.classList.remove("template");
        labelClone.classList.remove("template");
      
        newDiv.appendChild(inputClone);
        newDiv.appendChild(labelClone);
  
      })    
  
    }
  
    addItemTop.addEventListener("click", function(){
      
      getvals("","/user").then(response => setResponse(response));   
  
    })
  
  selectAll.addEventListener("click", function(item){
  
  
    var isChecked = selectAll.checked;
    allCheckboxes.forEach(function (item){
  
      if(isChecked){
        item.checked = true;								
      }
      else{
        item.checked = false;				
      }	
  
    })  
  })	  

})


