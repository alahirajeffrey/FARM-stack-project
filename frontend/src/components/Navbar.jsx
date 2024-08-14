import Button from "./Button";

const Navbar = () => {
  const addMenuItem = () => {
    console.log("button in navbar clicked");
  };

  return (
    <div className="grid grid-cols-3 gap-4 bg-blue-800 py-3 ">
      <div className="col-span-2 px-5 font-black text-3xl ">
        Sholly Restaurant Menu
      </div>
      <Button title={"Add Menu"} onClick={addMenuItem} />
    </div>
  );
};

export default Navbar;
