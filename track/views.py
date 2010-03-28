# Create your views here.
from django.http import *
from models import *
from django.template import Context, loader
import datetime
import time


def list_open_issues(request):
#    issues = issue.objects.filter(status=OPEN_STATUS)
    issues = issue.objects.exclude(status=CLOSED_STATUS).order_by('updated')
    template = loader.get_template('openissues.html')
    c = Context({
        'issues':issues
    })
    
    return HttpResponse (template.render(c))

def view_issue(request, issueid):
    #if 1:
    try:
        i = issue.objects.get(id = issueid)
        template = loader.get_template('issue.html')
        
        c = Context({
            'issue':i
        })
        
        return HttpResponse (template.render(c))
    except:
        return HttpResponseRedirect ("/tracker/")
    

def update_issue(request):
    if 1:
        od = request.POST['od']
        statusupdate = request.POST['su']
        issid = request.POST['id']
	mentor = request.POST['assign']
        i = issue.objects.get(id = issid)
        #i.ongoingNotes = od
	if (od != ""):
		i.initialDesc += "\n" + datetime.datetime.now().strftime("[%H:%M:%S]: ")   + od
	i.ongoingNotes = ""
        i.status = int(statusupdate)
	if (mentor != i.assignedTo):
		i.initialDesc += "\n" + datetime.datetime.now().strftime("[%H:%M:%S]: Assigned mentor changed from ") + i.assignedTo + " to " + mentor
		i.assignedTo = mentor
        i.save()
        if (i.status == CLOSED_STATUS):
            return HttpResponseRedirect("/tracker/")
        else:
            return HttpResponseRedirect("/tracker/viewissue/"+str(i.id))
    #except:
    #return HttpResponse("bad request", status=500)

def create_issue_echoer(request):
    template = loader.get_template("createissue.html")
    context = Context ({})
    return HttpResponse(template.render(context))
    
def create_issue(request):
    if 1:
    #try:
        teamnumber = request.POST['tn']
        longdesc = request.POST['longdesc']
        shortdesc = request.POST['shortdesc']
        i = issue()
        i.team = teamnumber
        i.shortDesc = shortdesc
        i.initialDesc = longdesc
        i.status = OPEN_STATUS
        i.ongoingNotes = ""
	i.assignedTo = ""
        i.save()
        return HttpResponseRedirect("/tracker/viewissue/"+str(i.id))
    #except:
#	return HttpResponseRedirect("/tracker/createissueform")
        
def allissues(request):
    issues = issue.objects.all()
    template = loader.get_template('openissues.html')
    c = Context({
        'issues':issues
    })
    
    return HttpResponse (template.render(c))
