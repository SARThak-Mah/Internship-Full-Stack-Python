import React, { useState } from "react";
import PrimeUser from "./PrimeUser";
import GuestUser from "./GuestUser";

export default function LoginPage() {
  let [IsLogin, setIsLogin] = React.useState(true);
  let login = () => {
    setIsLogin(true);
  };
  let logout = () => {
    setIsLogin(false);
  };
  return (
    <div>
      {(() => {
        if (IsLogin) {
          return <PrimeUser name="Prime User" data={logout} />;
        } else {
          return <GuestUser name="Guest User" data={login} />;
        }
      })()}
    </div>
  );
}
