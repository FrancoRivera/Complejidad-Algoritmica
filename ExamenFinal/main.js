        function createTable(rows, cols, data, dest,id ){
             var new_table = $('<table></table>').attr({ id: "basicTable",class:"table table-hover"});
            var tr = [];
            for (var i = 0; i < rows; i++) {
                var row = $('<tr></tr>').attr({ class: ["class1"].join(' ') }).appendTo(new_table);
            if (i==0) {
              for (var j = 0; j < cols; j++) {
                    $('<th></th>').text(data[i][j]).attr({class:["info"]}).appendTo(row);
                }
            }else {
                for (var j = 0; j < cols; j++) {
                    $('<td></td>').text(data[i][j]).attr("id", String(id+"_"+i+"_"+j)).appendTo(row);
                }
        }
            }
            $(dest).slideUp()
            $(dest).append(new_table)
            $(dest).slideDown()
        
        }
        function drawArrow(ctx,color, fromx, fromy, tox, toy){
                //variables to be used when creating the arrow

                var headlen = 10;
                var weight=3;
                var angle = Math.atan2(toy-fromy,tox-fromx);
                
                //starting path of the arrow from the start square to the end square and drawing the stroke
                ctx.beginPath();
                ctx.moveTo(fromx, fromy);
               //f ctx.lineTo(tox, toy);
                ctx.bezierCurveTo(fromx+(tox-fromx)/3,toy,fromx+(tox-fromx)/2,toy,tox,toy);
                ctx.strokeStyle = color;
                ctx.lineWidth = weight;
                ctx.stroke();

                //starting a new path from the head of the arrow to one of the sides of the point
                ctx.beginPath();
                ctx.moveTo(tox, toy);
                ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),toy-headlen*Math.sin(angle-Math.PI/7));

                //path from the side point of the arrow, to the other side point
                ctx.lineTo(tox-headlen*Math.cos(angle+Math.PI/7),toy-headlen*Math.sin(angle+Math.PI/7));

                //path from the side point back to the tip of the arrow, and then again to the opposite side point
                ctx.lineTo(tox, toy);
                ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),toy-headlen*Math.sin(angle-Math.PI/7));

                //draws the paths created above
                ctx.strokeStyle = color;
                ctx.lineWidth = weight;
                ctx.stroke();
                ctx.fillStyle = color;
                ctx.fill();
            }

        function Knapsack(){
        var input = $("[input='knapsack']").val()
        var input_lines = input.split("\n")
        var max_weight = parseInt(input_lines[0])
        var n = parseInt(input_lines[1]) //primera linea es cant de datos
        var arreglo_items = []
        for (var i = 2; i < 2+n; i++){
            arreglo_items.push(input_lines[i].trim().split(","))
        }
        arreglo_items.sort(function(a,b){return a[1]-b[1]})
        matriz = []
        for (var i = 0; i<n; i++){
            matriz.push(new Array(max_weight+1))
        }

        for (var fila = 0; fila < matriz.length; fila++){
            valor_item = parseInt(arreglo_items[fila][0])
            peso_item = parseInt(arreglo_items[fila][1])
            for (var peso=0; peso < matriz[0].length; peso++){
                if (peso_item <= peso){
                    if (fila == 0){ //si es la primera fila
                        nuevo_valor = valor_item
                        }
                    else{
                        nuevo_valor = Math.max(valor_item+matriz[fila-1][peso-peso_item],matriz[fila-1][peso])
                        }
                }
                else{
                    if (fila == 0){ //si es la primera fila
                        nuevo_valor = 0
                        }
                    else{
                    nuevo_valor = matriz[fila-1][peso]
                        }
                     }
                matriz[fila][peso] = nuevo_valor
               
            } 

        }
        header = ["Item"]
        for (var i = 0; i < max_weight+1;i++){
            header.push(i)
        }
        matriz.unshift(header)
        for (var i = 1; i < arreglo_items.length+1; i++){
             matriz[i].unshift("Valor: "+ arreglo_items[i-1][0] + " Peso: "+arreglo_items[i-1][1])
        }
        $("[resultado='knapsack']").html("<h3>Resultado</h3> (en rojo los items en la mochila)")
        createTable(n+1, max_weight+2, matriz, "[resultado='knapsack']", "knapsack")
        
        it_item = n
        it_weight = max_weight+1
        best = matriz[it_item][it_weight]
        while(best>=0 ){
            if (matriz[it_item-1][it_weight]==best){
                if (it_item==1) {
                    $("#knapsack_"+it_item+"_"+it_weight).addClass("btn btn-danger");
                    $("#knapsack_"+it_item+"_"+0).addClass("btn btn-danger");
                    break;
                }
                it_item -=1
                
            }
            else{
                $("#knapsack_"+it_item+"_"+it_weight).addClass("btn btn-danger")
                $("#knapsack_"+it_item+"_"+0).addClass("btn btn-danger");
                it_weight = it_weight-parseInt(arreglo_items[it_item-1][1])
                it_item -=1
            }
            best = matriz[it_item][it_weight]
        }
 
    }

        class UFDS{
            constructor() {
                this.size = 0;
                this.parent = []
                this.rank = []
                
              }
            initSet(size){  
                this.size = size
                for (var i = 0; i < size; i++){
                    this.parent.push(i)
                    this.rank.push[0]
                }
            }
            findRoot(x){
                if (this.parent[x] != x){
                   x = this.findRoot(this.parent[x]) 
                }
                return this.parent[x]
            }
            isSameSet(x, y){
                return this.findRoot(x) == this.findRoot(y);
            }
            
            unionSet(x,y){
                x = this.findRoot(parseInt(x))
                y = this.findRoot(parseInt(y))
                if (this.isSameSet(x,y)) return
                if (this.rank[x] > this.rank[y]) this.parent[y] = x
                else{
                    this.parent[x] = y
                    if (this.rank[x] = this.rank[y]) this.rank[y] += 1
                }
     
            }
        }
 
        $("#go_animate_UFDS").click(async function(){
            $("[input='UFDS']").html("10\n1\n4, 3")
             $("#go_UFDS").click()
            await sleep(1000);
            $("[input='UFDS']").html("10\n2\n4, 3\n1, 5")
             $("#go_UFDS").click()
            await sleep(1000);
            $("[input='UFDS']").html("10\n3\n4, 3\n1, 5\n5, 4")
             $("#go_UFDS").click()
            await sleep(1000);
            $("[input='UFDS']").html("10\n5\n4, 3\n1, 5\n5, 4\n7, 5\n6,2")
             $("#go_UFDS").click()
            await sleep(1000);
            $("[input='UFDS']").html("10\n6\n4, 3\n1, 5\n5, 4\n7, 5\n6,2\n8,9")
             $("#go_UFDS").click()
            await sleep(1000);
            $("[input='UFDS']").html("10\n7\n4, 3\n1, 5\n5, 4\n7, 5\n6,2\n8,9\n0,2")
             $("#go_UFDS").click()
            await sleep(1000);
            $("[input='UFDS']").html("10\n8\n4, 3\n1, 5\n5, 4\n7, 5\n6,2\n8,9\n0,2\n9,4")
             $("#go_UFDS").click()
            await sleep(1000);
            $("[input='UFDS']").html("10\n9\n4, 3\n1, 5\n5, 4\n7, 5\n6,2\n8,9\n0,2\n9,4\n3,0")
             $("#go_UFDS").click()
            await sleep(1000);
        })
        $("#go_UFDS").click(function(){
          
             var input = $("[input='UFDS']").val()
            var input_lines = input.split("\n")
            var ufds = new UFDS()
            ufds.initSet(parseInt(input_lines[0]))
            var n = parseInt(input_lines[1])
            var unions = []
            for (var i = 2; i < 2+n; i++){
                unions.push(input_lines[i].trim().split(","))
            }
            for (var i = 0; i < n; i++){
               ufds.unionSet(unions[i][0], unions[i][1])
            }
            
            var roots = []
            var children =[]
            for (var i = 0; i <  input_lines[0]; i++) children.push([])
            for (var i = 0; i < input_lines[0]; i++)if(!roots.includes(ufds.findRoot(i))) roots.push(ufds.findRoot(i))
            for (var i = 0; i < input_lines[0]; i++)if (ufds.findRoot(i) != i) children[roots.indexOf(ufds.findRoot(i))].push(i)    

            $("[resultado='UFDS']").html("<h2>Resultado</h2>")
            $("[resultado='UFDS']").append("<canvas id='canvas_ufds'></canvas>")
            var canvas = document.getElementById("canvas_ufds")
            canvas.height = 300
            canvas.width = 600
            var ctx = canvas.getContext("2d")
            ctx.font = "20px Georgia"
            for (var i = 1; i < roots.length+1; i++){
                ctx.fillStyle = "red"
                x_p = i*(canvas.width/(roots.length+1))
                ctx.fillRect(x_p, 0, 30, 30)
                 ctx.fillStyle = "black"
                ctx.fillText(roots[i-1],x_p+10, 25, 100)
                for (var j = 0; j < children[i-1].length; j++){
                    ctx.fillStyle = "red"
                    x = x_p+x_p/(children[i-1].length*i)*j
                    x = x-x_p/i/2
                    
                    ctx.fillRect(x, 100, 30, 30)
                    ctx.fillStyle = "black"
                    ctx.fillText(children[i-1][j],x+10, 125, 100)
                    ctx.moveTo(x+10, 110)
                    ctx.lineTo(i*(canvas.width/(roots.length+1))+10, 25)
                    ctx.stroke()
                }
            }
        })
        $("#go_floyd").click(function(){
            var input = $("[input='floydwarshall']").val()
            var input_lines = input.split("\n")
            var size = parseInt(input_lines[0])
            var n = parseInt(input_lines[1]) //primera linea es cant de datos
            var edges = []
            var grafo = new Graph(size)
            for (var i = 2; i < 2+n; i++){
                grafo.addEdge(input_lines[i].trim().split(","))
            }
            
            $("[resultado='floydwarshall']").html("<canvas id='canvas_floydwarshall'></canvas>")
             $("[resultado='floydwarshall']").append("<div class='col-md' id='table_warshall'></div>")
            grafo.drawGraph("canvas_floydwarshall")
            
            grafo.FloydWarshall("#table_warshall")

        })

        class Graph{
            constructor(size){
                this.size = size;
                this.NODOS = []
                for (var i =0; i<size;i++) this.NODOS.push(i)
                this.EDGES = []
                this.posNODOS=[];
                this.d = []
                 for (var i =0; i<size;i++) this.d.push(Infinity)
                
            }
            addEdge(edge){
                this.EDGES.push([parseInt(edge[0]),parseInt(edge[1]),parseInt(edge[2])])
            }
            drawGraph(dest){
            var canvas = document.getElementById(dest)
            canvas.height = 400
            canvas.width = 600
            var ctx = canvas.getContext("2d")
            ctx.font = "20px Georgia"          
            for (var i = 0; i < this.size; i++){
                ctx.fillStyle = "red"
                var node_y = 100
                var node_x = i*(canvas.width/4)
                if (i >= 4){node_x=(i-4)*(canvas.width/4);node_y=200}
                if (i >= 8){node_x=(i-8)*(canvas.width/4);node_y=300}
                ctx.fillRect(node_x, node_y, 30, 30)
                this.posNODOS.push([node_x+10,node_y])
                
            }
            for (var i = 0; i < this.EDGES.length; i++){
                var u = this.EDGES[i][0]
                var v = this.EDGES[i][1]
                var w = this.EDGES[i][2]
                
                drawArrow(ctx,"#4480e0", this.posNODOS[u][0],this.posNODOS[u][1],this.posNODOS[v][0]+15,this.posNODOS[v][1]+15)
                var dist = (this.posNODOS[v][0]-this.posNODOS[u][0]+15)/2
                var slope = (this.posNODOS[v][1]+15-this.posNODOS[u][1])/2
                ctx.fillStyle = "black";
                ctx.fillText(String(w),dist+this.posNODOS[u][0], this.posNODOS[u][1]+slope)
            } 
                                
            for (var i = 0; i < this.size; i++){
                ctx.fillStyle = "black"
                ctx.fillText(i, this.posNODOS[i][0],this.posNODOS[i][1]+20)
                
            }
            }
            
            BellmanFord(source, dest){
           
                this.d[source] = 0;
                for (var i = 0; i < this.size-1; i++){
                     for (var j = 0; j < this.EDGES.length; j++){
                         if (this.d[this.EDGES[j][0]]+this.EDGES[j][2]< this.d[this.EDGES[j][1]])
                            this.d[this.EDGES[j][1]] = this.d[this.EDGES[j][0]] + this.EDGES[j][2]
                            //this.P[this.EDGES[j][1]] = this.EDGES[j][0]
                     }
                }
                for (var i = 0; i < this.size-1; i++){
                     for (var j = 0; j < this.EDGES.length; j++){
                         if (this.d[this.EDGES[j][0]]+this.EDGES[j][2]< this.d[this.EDGES[j][1]])
                            alert("Graph contains negative cycle \n")
                     }
                }
                 var canvas = document.getElementById(dest)
                  var ctx = canvas.getContext("2d")
                for (var i = 0; i < this.d.length; i++){
                     ctx.font = "20px Georgia"    
                    ctx.fillStyle ="green"
                    ctx.fillText(this.d[i], this.posNODOS[i][0], this.posNODOS[i][1])
                }
            }
            
            Kruskal(dest){
                var canvas = document.getElementById(dest)
                var ctx = canvas.getContext("2d")
                var ufds = new UFDS()
                ufds.initSet(this.size)
                var mst_weight = 0
                this.EDGES.sort(function(a,b){return a[2]-b[2]})
                console.log(this.EDGES)
                for (var i = 0; i < this.EDGES.length; i++){
                    var u = this.EDGES[i][0]
                    var v = this.EDGES[i][1]
                    var w = this.EDGES[i][2]
                    if (!ufds.isSameSet(u,v)){
                        drawArrow(ctx,"#44e092", this.posNODOS[u][0],this.posNODOS[u][1],this.posNODOS[v][0]+15,this.posNODOS[v][1]+15)
                       mst_weight += w
                        ufds.unionSet(u,v)
                    }
                    
                }
                console.log(ufds.parent)

            ctx.font = "30px Georgia"   
            ctx.fillText("MST: " + mst_weight, 50, 50)
                
            }
            
            Prim(dest){}
            
            Johnson(dest){}
            
            Djikstra(dest){}
            
            FloydWarshall(dest){
                var matriz = []
                for (var i= 0; i < this.size; i++){
                    matriz.push(new Array(this.size).fill(Infinity))
                }
                for (var i = 0; i < this.EDGES.length; i++){
                    matriz[this.EDGES[i][0]][this.EDGES[i][1]] = this.EDGES[i][2]
                }
                for (var k = 0; k < this.size; k++){
                      for (var i = 0; i < this.size; i++){
                            for (var j = 0; j < this.size; j++){
                                var ns = matriz[i][k] + matriz[j][k]
                                if (matriz[i][j] > ns) matriz[i][j] = ns
                            }
                      }
                }
                var header = ["NODE"]
                    for (var i = 0; i < this.size+1;i++){
                        header.push(i)
                    }
                matriz.unshift(header)
                 for (var i = 0; i < this.size;i++){
                        matriz[i+1].unshift(i)
                    }
                
                 createTable(this.size+1, this.size+1, matriz, dest, "floydwarshall")
            }
           
            
        }