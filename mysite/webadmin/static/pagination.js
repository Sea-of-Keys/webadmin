
document.addEventListener("DOMContentLoaded", function(){   

    function SetPagination(next,previous,param){

        var previous_button = document.getElementById(previous);
        var next_button = document.getElementById(next);        

        if(previous_button){
            previous_button.onclick = function(){previous_page(param,previous_button)};
        }
        if(next_button){
            next_button.onclick = function(){next_page(param,next_button)};   
        }    

    }  

    function next_page(param,button){   
            
            var url = new URL(window.location.href);
            var search_params = url.searchParams;        
            search_params.set(param, button.dataset.page);
            url.search = search_params.toString();        
            var new_url = url.toString();      
            window.location = new_url;          
    }

    
    function previous_page(param,button){            
     
            
        var url = new URL(window.location.href);
        var search_params = url.searchParams;        
        search_params.set(param, button.dataset.page);
        url.search = search_params.toString();        
        var new_url = url.toString();  
        window.location = new_url;  
}   

class Paginator {
    constructor(next, previous, param) 
    {
        this.next = next;
        this.previous = previous;
        this.param = param;
    }  

   


  }

    var paginators = []

    paginators.push(new Paginator("team-next","team-previous","teamPage"))
    paginators.push(new Paginator("history-next","history-previous","historyPage"))
    paginators.push(new Paginator("teams-next","teams-previous","teamPage"))
    paginators.push(new Paginator("users-next","users-previous","userPage"))
    paginators.push(new Paginator("user-history-next","user-history-previous","userHistory"))
    paginators.push(new Paginator("rooms-next","rooms-previous","roomsPage"))
    paginators.push(new Paginator("room-team-next","room-team-previous","teamRoomsPage"))
    paginators.push(new Paginator("team-user-next", "team-user-previous","teamUsersPage"))

    paginators.forEach(function (item){        

        SetPagination(item.next,item.previous,item.param)

    })
   
  

})