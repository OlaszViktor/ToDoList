# ToDoList Alkalmazás
Név: Olasz Viktor Ferenc
Neptun Kód: CX773M

## Rövid Leírás
Ez az alkalmazás egy egyszerű feladatlista kezelőt valósít meg, amely lehetővé teszi a felhasználó számára, hogy feladatokat adjon hozzá, távolítson el, mentse és töltsön be egy fájlból.
A `tkinter` grafikus felhasználói felületet, `sqlite3` adatbázist és a `tkcalendar` modult használja a dátum kiválasztásához.

## Modulok
- `tkinter`: A grafikus felhasználói felület létrehozásához.
- `sqlite3`: Az adatbázis-kezeléshez, a feladatok tárolásához és lekérdezéséhez.
- `random`: Véletlenszerű feladat kiválasztásához.
- `os`: Fájlok és könyvtárak kezeléséhez.
- `tkcalendar`: A dátum kiválasztásának megkönnyítéséhez egy naptár widget segítségével.

## Függvények
- `add_task()`: Feladat hozzáadása a listához és az adatbázishoz.
- `remove_task()`: Kiválasztott feladat eltávolítása a listából és az adatbázisból.
- `save_tasks_to_file()`: A jelenlegi feladatok mentése egy szöveges fájlba.
- `load_tasks_from_file()`: Feladatok betöltése egy szöveges fájlból, megakadályozza a duplikációkat.
- `select_random_task()`: Véletlenszerű feladat kiválasztása és megjelenítése egy felugró ablakban.
- `befejezve()`: A kiválasztott feladat megjelölése, mint "befejezve".

## Egyéni Osztály
- `TaskManager`: Osztály a feladatok kezeléséhez, amely tartalmazza az adatbázisműveleteket, mint például a feladatok hozzáadása és eltávolítása.

## Használat
Futtassa a `Beadando_Olasz_Viktor_Ferenc_CX773M.py` fájlt, és használja a grafikus felhasználói felületet a feladatok kezeléséhez. 
Adhat hozzá új feladatokat, eltávolíthatja a meglévőket, mentheti a feladatokat egy fájlba, betöltheti a feladatokat egy fájlból és kiválaszthat egy véletlenszerű feladatot.
