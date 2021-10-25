pipeline { 
agent any 
    triggers
    {
        pollSCM('0 0 * * *')
    }
    stages 
    { stage("Compile") 
        { steps 
            {echo "Python compile done" } } 
    stage("Unit test") 
        { steps 
            { sh "python test_circle.py" } } 
    } 
} 