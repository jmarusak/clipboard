package main

import (
	"html/template"
	"net/http"
)

type Entry struct {
	Content string
}

type Data struct {
	LastEntry string
	Entries []Entry
}	

func main() {
	var data Data
	var entry Entry

	tmpl := template.Must(template.ParseFiles("form.html"))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == http.MethodPost {
			r.ParseForm()
			entry.Content = r.FormValue("entry")
			data.Entries = append(data.Entries, entry)
			data.LastEntry = data.Entries[len(data.Entries)-1].Content
		}

		tmpl.Execute(w, data)
	})

	http.ListenAndServe(":8080", nil)
}
