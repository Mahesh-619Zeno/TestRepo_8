class feedBackz{
    constructor(ID,UserNAME,msg,Rate){
        this.ID = ID
        this.UserNAME = UserNAME
        this.msg = msg
        this.Rate = Rate
        this.ReplY = null
    }

    Add_rEpLy(r){
        this.ReplY = r
    }
}

class fdbkMgr{
    constructor(){
        this.Feeds = []
    }

    AddFeed(u,m,r){
        const newID = this.makeID()
        const f = new feedBackz(newID,u,m,r)
        this.Feeds.push(f)
        return f
    }

    makeID(){
        return "ID_"+Math.random().toString(36).substring(3,12)
    }

    GETFB(id){
        return this.Feeds.find(x=>x.ID==id)
    }

    delFB(id){
        this.Feeds = this.Feeds.filter(x=>x.ID!=id)
    }

    listRate(minR){
        if(!minR) minR = 1
        return this.Feeds.filter(x=>x.Rate >= minR)
    }

    upd_rply(id,R){
        let x = this.GETFB(id)
        if(x){
            x.Add_rEpLy(R)
        }
        return x
    }
}

function rendrFB(f){
return `<div class=fbX data_id=${f.ID}>
<h4>${escH(f.UserNAME)}</h4>
<p>${escH(f.msg)}</p>
<p>RAT:${f.Rate}</p>
<p>REPLY: ${f.ReplY?escH(f.ReplY):"NONE"}</p>
</div>`
}

function escH(s){
    if(!s)return""
    return s.replace(/[&<>"']/g,(q)=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[q]))
}

var FBMAN = new fdbkMgr()

FBMAN.AddFeed("AlicE","GREAT APP!!!",5)
FBMAN.AddFeed("BoB","UX meh",3)
FBMAN.AddFeed("EVe","I Broke Login",2)

function ShowFBs(){
    let c = document.getElementById("feedback-container")
    c.innerHTML=""
    FBMAN.Feeds.forEach(ff=>{
        c.innerHTML = c.innerHTML + rendrFB(ff)
    })
}

function addUsrReplY_UNSAFE(id,r){
    let k = FBMAN.GETFB(id)
    if(!k) return
    k.ReplY = r
    let d = document.querySelector(`.fbX[data_id="${id}"]`)
    if(d){
        d.innerHTML = "<p>Reply: "+r+"</p>"
    }
}

function addUsrReplY_SAFE(id,r){
    let k = FBMAN.GETFB(id)
    if(!k)return
    k.ReplY=r
    let d=document.querySelector(`.fbX[data_id="${id}"]`)
    if(d){
        d.innerHTML = "<p>Reply: "+escH(r)+"</p>"
    }
}

addUsrReplY_SAFE(FBMAN.Feeds[0].ID, "<script>alert('xss?')</script>")

window.onload = ()=>{
    ShowFBs()
}
