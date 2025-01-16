from flask import Flask, redirect, render_template, request, url_for, flash
from DB_Operations import fetch_all_items, insert_item, fetch_item_by_id, update_item, delete_item

app = Flask(__name__)
app.secret_key = "pendidikann"


@app.route("/")
def index():
    programs = fetch_all_items()
    return render_template("index.html", programs=programs)

@app.route('/add_item', methods=["POST","GET"])
def add_item():
    if request.method == 'POST':
        namaProgram = request.form['nama_program']
        kelas = request.form['kelas']
        durasi = request.form['durasi']
        biaya = request.form['biaya']
        # insert item kedalam db
        insert_item(namaProgram,kelas,durasi,biaya)
        flash('Item Added Succesfully!')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=["GET","POST"])
def edit_item(id):
    item = fetch_item_by_id(id)
    if request.method == 'POST':
        namaProgram = request.form['nama_program']
        kelas = request.form['kelas']
        durasi = request.form['durasi']
        biaya = request.form['biaya']
        #update item
        update_item(id,namaProgram,kelas,durasi,biaya)
        flash("Item Updated Succesfully")
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<id>', methods=["GET", "POST"])
def delete_item_route(id):
    delete_item(id)
    flash('Item Deleted Successfully!')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)