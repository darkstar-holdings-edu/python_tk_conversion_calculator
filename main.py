from app import App


def main() -> None:
    app = App()

    def convert_miles_to_km() -> None:
        value = input_1.get()
        if not value.isdigit():
            label_3.config(text="NaN")
            return

        miles = int(value)
        km = miles * 1.609344

        label_3.config(text=f"{km:.2f}")

    input_1 = app.create_entry(width=10, row_pos=0, column_pos=1)

    app.create_label("Miles", row_pos=0, column_pos=2)
    app.create_label("is equal to", row_pos=1, column_pos=0)

    label_3 = app.create_label("0", row_pos=1, column_pos=1)
    app.create_label("Km", row_pos=1, column_pos=2)

    app.window.bind("<Return>", lambda _: convert_miles_to_km())
    app.window.bind("<KP_Enter>", lambda _: convert_miles_to_km())

    app.create_button(
        "Calculate",
        row_pos=2,
        column_pos=1,
        callback=convert_miles_to_km,
    )

    app.mainloop()


if __name__ == "__main__":
    main()
