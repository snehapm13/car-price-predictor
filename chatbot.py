import streamlit as st


def format_counts(data):

    result = []

    for name, count in data.items():
        result.append(
            f"{name}: {count}"
        )

    return ", ".join(result)


def get_chatbot_response(question, df):

    question = question.lower().strip()

    # Dataset information
    if (
        "dataset" in question
        or "data information" in question
    ):
        return (
            f"The dataset contains {df.shape[0]} cars "
            f"and {df.shape[1]} columns. "
            f"The target column is selling_price."
        )

    # Total records
    elif (
        "how many cars" in question
        or "total cars" in question
        or "total records" in question
    ):
        return (
            f"The dataset contains "
            f"{len(df)} car records."
        )

    # Column names
    elif (
        "column" in question
        or "features" in question
    ):
        columns = ", ".join(df.columns)

        return (
            f"The dataset columns are: {columns}."
        )

    # Brand information
    elif "brand" in question:

        brand_counts = (
            df["brand"]
            .value_counts()
            .to_dict()
        )

        brands = format_counts(brand_counts)

        return (
            f"Available car brands are: {brands}."
        )

    # Fuel information
    elif "fuel" in question:

        fuel_counts = (
            df["fuel_type"]
            .value_counts()
            .to_dict()
        )

        fuels = format_counts(fuel_counts)

        return (
            f"Fuel types in the dataset are: {fuels}."
        )

    # Transmission information
    elif "transmission" in question:

        transmission_counts = (
            df["transmission"]
            .value_counts()
            .to_dict()
        )

        transmissions = format_counts(
            transmission_counts
        )

        return (
            "Transmission types are: "
            f"{transmissions}."
        )

    # Average price
    elif (
        "average price" in question
        or "mean price" in question
    ):
        average_price = (
            df["selling_price"].mean()
        )

        return (
            "The average selling price is "
            f"₹{average_price:,.0f}."
        )

    # Maximum price
    elif (
        "maximum price" in question
        or "highest price" in question
        or "costliest" in question
    ):
        maximum_price = (
            df["selling_price"].max()
        )

        return (
            "The highest selling price is "
            f"₹{maximum_price:,.0f}."
        )

    # Minimum price
    elif (
        "minimum price" in question
        or "lowest price" in question
        or "cheapest" in question
    ):
        minimum_price = (
            df["selling_price"].min()
        )

        return (
            "The lowest selling price is "
            f"₹{minimum_price:,.0f}."
        )

    # Manufacturing year
    elif (
        "year" in question
        or "newest" in question
        or "oldest" in question
    ):
        oldest_year = df["year"].min()
        newest_year = df["year"].max()

        return (
            f"The cars are manufactured between "
            f"{oldest_year} and {newest_year}."
        )

    # Mileage information
    elif "mileage" in question:

        average_mileage = (
            df["mileage"].mean()
        )

        return (
            "Mileage shows how far a car can travel "
            "using one litre of fuel. "
            f"The average dataset mileage is "
            f"{average_mileage:.1f} KM/L."
        )

    # Engine information
    elif "engine" in question:

        minimum_engine = df["engine"].min()
        maximum_engine = df["engine"].max()

        return (
            "Engine capacity is measured in CC. "
            f"The dataset contains engines from "
            f"{minimum_engine:.0f} CC to "
            f"{maximum_engine:.0f} CC."
        )

    # Owner information
    elif "owner" in question:

        maximum_owners = df["owners"].max()

        return (
            "Previous owners show how many people "
            "owned the car earlier. "
            f"The maximum in this dataset is "
            f"{maximum_owners} owners."
        )

    # Car price factors
    elif (
        "price factor" in question
        or "affect price" in question
        or "price depends" in question
    ):
        return (
            "Car price can depend on brand, year, "
            "kilometres driven, fuel type, "
            "transmission, owners, engine, mileage, "
            "maximum power and seats."
        )

    # Show complete dataset
    elif (
        "show data" in question
        or "show all records" in question
    ):
        return (
            "You can open View Complete Dataset "
            "below the chatbot."
        )

    # Default answer
    else:
        return (
            "You can ask about total cars, columns, "
            "brands, fuel types, transmission, "
            "average price, highest price, lowest "
            "price, mileage, engine or price factors."
        )


def show_chatbot(df):

    st.subheader("Car Information Chatbot")

    st.write(
        "Ask a question about cars or the dataset."
    )

    # Create chat history
    if "chat_messages" not in st.session_state:

        st.session_state.chat_messages = []

    # Display previous messages
    for message in st.session_state.chat_messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])

    # Get user question
    question = st.chat_input(
        "Ask about the car dataset"
    )

    if question:

        # Save and display user question
        st.session_state.chat_messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.write(question)

        # Get chatbot answer
        answer = get_chatbot_response(
            question,
            df
        )

        # Save and display chatbot answer
        st.session_state.chat_messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.write(answer)

    # Display complete dataset
    with st.expander("View Complete Dataset"):

        st.dataframe(
            df,
            use_container_width=True
        )