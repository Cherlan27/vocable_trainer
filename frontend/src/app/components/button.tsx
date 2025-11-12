"use client";

import './button.css';

type ButtonProps = {
    title: string;
    onClickButton?: () => void;
}  & React.InputHTMLAttributes<HTMLInputElement>;

export function MyButton(
    { title, onClickButton }: ButtonProps
) {
    return (
        <button className="my-button" onClick={onClickButton}>{title}</button>
    )
}

export function MyButton2(
    { title, onClickButton }: ButtonProps
) {
    return (
        <button className="my-button2" onClick={onClickButton}>{title}</button>
    )
}
