function whoAmI(picture, number){
    	
    	if(picture =='baby1')
    	{
    		document.getElementById('response' + number).innerHTML ="Dylan";
    	}
    	else if(picture =='baby2')
    	{
    		document.getElementById('response'+ number).innerHTML ="Tristan";
    	};

        document.getElementById('response' + number).style.color = "red";
    };


