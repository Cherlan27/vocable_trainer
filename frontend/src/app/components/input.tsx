import React, { useState } from "react";
import "./input.css";

export default function InputField(
    {
        id,
        value,
        onInputChange
    }:
    { id?: string, value: string, onInputChange: (value: string) => void }
)
    {

    return (
        <input
            type="text"
            placeholder="Topic of new French words"
            className="input input-bordered w-full max-w-xs"
            id={id}
            value={value}
            onChange={(e) => onInputChange(e.target.value)}
        />
    );
}
