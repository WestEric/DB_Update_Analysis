# MusicDBUpdater
import pyodbc
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Music_DB_Updater:

    def __init__(self,root):
            # Label window
        root.title("Album Data Entry Program")
            
            # Create Frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
            
            # Create variables for entry fields
        self.title = StringVar()
        self.artist = StringVar()
        self.release = StringVar()
        self.genre = StringVar()
        self.flags = StringVar()

            # Create and place entry labels
        ttk.Label(mainframe, text="Album Title").grid(column=1, row=1, sticky=E)
        ttk.Label(mainframe, text="Artist").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Release Year").grid(column=1, row=3, sticky=E)
        ttk.Label(mainframe, text="Genre").grid(column=1, row=4, sticky=E)
        ttk.Label(mainframe, text="Flags").grid(column=1, row=5, sticky=E)

            # Create entry button
        ttk.Button(mainframe, text="Commit Record", command=self.commit_record).grid(column=1, row=6, columnspan=3, sticky=(E,W))

            # Create entry fields
        title_entry = ttk.Entry(mainframe, width=50, textvariable=self.title)
        artist_entry = ttk.Entry(mainframe, width=50, textvariable=self.artist)
        release_entry = ttk.Entry(mainframe, width=50, textvariable=self.release)
        genre_entry = ttk.Entry(mainframe, width=50, textvariable=self.genre)
        flags_entry = ttk.Entry(mainframe, width=50, textvariable=self.flags)
            
            # Place objects
        title_entry.grid(column=2, row=1, sticky=(W, E))
        artist_entry.grid(column=2, row=2, sticky=(W, E))
        release_entry.grid(column=2, row=3, sticky=(W, E))
        genre_entry.grid(column=2, row=4, sticky=(W, E))
        flags_entry.grid(column=2, row=5, sticky=(W, E))

            # Spacing
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

            # Start cursor in title field
        title_entry.focus()
    
    def check_valid_fields(self):
            album_title = str(self.title.get())
            album_artist = str(self.artist.get())
            album_release = int(self.release.get())
            album_genre = str(self.genre.get())
            album_flags = str(self.flags.get())

            1/len(self.title.get())
            1/len(self.artist.get())
            1/album_release
            1/len(self.genre.get())
            return album_title, album_artist, album_release, album_genre, album_flags
    
    def check_duplicate_entry(self):
         pass
    
    def clear_text(self):
        self.title = StringVar()
        self.artist = StringVar()
        self.release = StringVar()
        self.genre = StringVar()
        self.flags = StringVar()


    def commit_record(self):
        try:
            album_title, album_artist, album_release, album_genre, album_flags = Music_DB_Updater.check_valid_fields(self)

            commit_yes_no = messagebox.askquestion(message='Commit\nTitle: {}\nArtist: {}\nRelease Year: {}\nGenre: {}\nFlags: {}'.format(album_title, album_artist, album_release, album_genre, album_flags),
                                                   title='Commit Record?')
            if commit_yes_no == 'yes':
                try:    
                    cnxn = pyodbc.connect(r'DRIVER=Microsoft Access Driver (*.mdb, *.accdb);DBQ=C:\Users\ericm\Documents\Music.accdb')
                    cnxn_cursor = cnxn.cursor()
                    cnxn_cursor.execute('INSERT INTO Albums (title,artist,release,genre,flags) \
                    VALUES(?,?,?,?,?)',(album_title,album_artist,album_release,album_genre,album_flags))
                    cnxn.commit()
                    cnxn.close()
                    messagebox.showinfo(message='Update Successful!',title='Update Committed')
                    Music_DB_Updater.clear_text(self)
                except:
                     messagebox.showinfo(message='Unable to connect to database.',title='Connection Error')
        except:
            messagebox.showerror(message='Unable to commit to database.\nCheck field values and try again.',
                                 title='Unable to Commit Entry')
            
root = Tk()
Music_DB_Updater(root)
root.mainloop()