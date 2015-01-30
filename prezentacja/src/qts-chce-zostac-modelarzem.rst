:title: Qt(ś) chce zostać modelarzem?
:author: Mateusz Mikołajczyk
:css: _prezentacja.css

Qt(ś) chce zostać modelarzem?
=============================

Mateusz Mikołajczyk, PYRA, 30.01.2015

.. image:: images/temat.png

.. note:: Witajcie

----

.. image:: images/IMG_4623.JPG

.. note::
    Jako, że prezentacja w całości poświęcona jest pythonowi, ...

    ... powiem o swojej firmie

    pracownicy AYA Ghana

----

:data-x: r0
:data-z: -100
:data-rotate-x: 180

.. image:: images/IMG_2778.JPG

.. note::
    pracownicy AYA Ghana podczas wypłaty w programie LEAP

----

:data-x: r1600

.. image:: images/IMG_2865.JPG

.. note::
    pracownicy AYA Ghana podczas wypłaty w programie LEAP

----

:data-rotate-y: 90
:data-y: 600

:id: terminal

.. image:: images/terminal.png

.. note::
    tak wygląda praca przy terminalu

    sami piszemy firmware na urządzenia

    drukowanie fontów a endianess

----

:data-y: r1600
:data-rotate-x: 90

.. image:: images/lavare.jpg
.. note::
    brak programów do wystawiania faktur (off-line)
    stwierdziłem, że napiszę sam przy użyciu Qt i pythona

----

Qt + Python
===========

Dostępne dowiązania

* PyQt [Qt 4/5] (GPL)
* PySide [Qt 4] (LGPL)

.. note::
    * różnice licencyjne
    * jeśli ktoś chciałby użyć C++ - w Qt5 jest wbudowany moduł JSON
    * nacisk na Qt Quick i QML
    * w Qt5 wprowadzono wsparcie dla akceleracji sprzetowej przy wyswietlaniu grafiki
    * Qt5 koncentruje się na urządzeniach mobilnych

----

:id: qt5-doc

PyQt5
=====

.. image:: images/pyqt5-docs.png

.. code:: cpp

    // C++
    QVariant QStringListModel::​data(
        const QModelIndex & index,
        int role) const

.. code:: python

    # python
    class Foo(object):
        def data(self, index, role):
            # ...

.. note:: 
    * Niech nikogo nie zdziwi fakt, że dokumentacja do PyQt5 może być niekompletna.
    * Nie trzeba bać się odnośnika do dokumentacji od C++.
    * Translacja jest bardzo prosta

----

:id: model-intro

Co to jest model?
=================

.. image:: images/modelview-overview.png

.. note::
    * model trzyma nasze dane
    * podczas edycji uaktywnia się delegate
    * renderowaniem danych zajmuje się widok

----

Co to jest model? (cd)
======================

.. image:: images/modelview-models.png

.. note::
    odpowiednik tabelki to dict

----

.. image:: images/talk-is-cheap.jpg

.. note::
    enough is enough!

    idea przykładów: pokazać, jak za pomocą małych kroków na końcu osiągnąć funkcjonalność.

    każdy kolejny kod jest drobną modyfikacją poprzedniego

----

Do czego służą role?
====================

.. image:: images/roles.svg

(kod nr. 2)

.. note::
    * przykład: jedna kolumna (podatek VAT w produkcie) - 0.23 oraz 23%
    * przykład: klucz obcy (wyświetlamy tekstową reprezentację a wartość to id)

----

Do czego służy indeks?
======================

Czyli dodawanie / edycja / usuwanie obiektu
-------------------------------------------

(kod nr. 3)

----

Reużywalny model
================

Czyli o tym, jak stworzyć dynamiczny model
------------------------------------------

.. code:: python

    class CarModel(AbstractModel):
        columns = (
            ("manufactured", "Rok produkcji"),
            ("brand", "Marka")
        )

(kod nr. 4)

.. note::
    Długo trwało zanim wpadłem na pomysł jak to zrobić
    Info na stronie dokumentacji Qt w sekcji 'Inheriting models'

----

:id: delegate

Pokrywamy domyślną edycję w tabelce
===================================

Kod sponsorują:

* metoda flags()
* role Qt::EditRole i Qt::DisplayRole

.. code:: python

    class CarBrand(AbstractModel):
        columns = (
            ("id", "ID"),
            ("name", "Nazwa",)
        )

    class CarModel(AbstractModel):
        columns = (
            ("manufactured", "Rok produkcji"),
            ("brand", "Marka")
        )
        model_mapping = {"brand": CarBrand}

.. note::
    Implementacja metody 'flags' na modelu pozwala na edycję od razu w tabelce
    Domyslna implementacja tej metody na to nie zezwala.

----

.. image:: images/yawn-collage.jpg

----

Łączymy się z chmurą
====================

* serwer: bottle
* klient: requests / urllib to the rescue!